# Nest Patterns

Use this file when the main skill is not enough for controller, provider, DTO, or exception-flow details.

## Contents

- Thin controller, explicit service contract
- DTO validation and response boundaries
- Provider composition in a module
- Provider token naming
- Exception translation

## Thin controller, explicit service contract

```ts
@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  async create(@Body() dto: CreateUserRequestDto): Promise<UserResponseDto> {
    const user = await this.usersService.create(mapCreateUserRequest(dto));
    return toUserResponseDto(user);
  }
}
```

```ts
@Injectable()
export class UsersService {
  constructor(
    @Inject(USER_REPOSITORY)
    private readonly userRepository: UserRepository,
  ) {}

  async create(input: CreateUserCommand): Promise<User> {
    return this.userRepository.create(input);
  }
}
```

- Keep the controller responsible for route concerns.
- Keep transport-to-application mapping at the edge and keep persistence coordination inside the service.
- Inject repository or gateway abstractions instead of newing SDK clients inside methods.

## DTO validation and response boundaries

```ts
export class CreateUserRequestDto {
  @IsEmail()
  email!: string;

  @IsString()
  @MinLength(8)
  password!: string;
}

export class UserResponseDto {
  id!: string;
  email!: string;
}
```

- Use request DTOs to validate incoming shape at the edge.
- Return response DTOs or serialized objects instead of raw entities.
- Keep validation rules on DTOs and leave business invariants to services.

## Provider composition in a module

```ts
@Module({
  controllers: [UsersController],
  providers: [
    UsersService,
    {
      provide: USER_REPOSITORY,
      useClass: PrismaUserRepository,
    },
  ],
  exports: [UsersService],
})
export class UsersModule {}
```

- Export the service when other modules need the use case.
- Avoid exporting infrastructure providers unless cross-module consumption is intentional.
- Prefer a focused module surface over a catch-all shared module.

## Provider token naming

```ts
export const USER_REPOSITORY = Symbol('USER_REPOSITORY');
```

- Prefer an existing repository token convention when the project already has one.
- Otherwise use feature-local uppercase constants or symbols that describe the dependency contract, not the implementation class.
- Keep tokens close to the module or provider contract that owns them.

## Exception translation

```ts
@Injectable()
export class UsersService {
  constructor(
    @Inject(USER_REPOSITORY)
    private readonly userRepository: UserRepository,
  ) {}

  async getById(id: string): Promise<User> {
    const user = await this.userRepository.findById(id);
    if (!user) {
      throw new UserNotFoundError(id);
    }
    return user;
  }
}

@Catch(UserNotFoundError)
export class UserNotFoundFilter implements ExceptionFilter {
  catch(exception: UserNotFoundError, host: ArgumentsHost): void {
    const response = host.switchToHttp().getResponse<Response>();
    response.status(404).json({ message: exception.message });
  }
}
```

- Raise meaningful application errors in the service layer.
- Translate them once near the transport boundary.
- Keep filters simple and predictable; do not bury business branching in them.
