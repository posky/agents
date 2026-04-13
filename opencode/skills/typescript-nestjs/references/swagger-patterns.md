# Swagger Patterns

Use this file when the main skill is not enough for controller endpoint documentation or DTO field annotations.

## Contents

- Controller endpoint decorators
- DTO field documentation
- Wrapped and paginated responses

## Controller endpoint decorators

```ts
@ApiTags('users')
@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Post()
  @ApiOperation({
    summary: 'Create a user',
    description: 'Create a new user from the validated request payload.',
  })
  @ApiCreatedResponse({
    description: 'User created successfully',
    type: UserResponseDto,
  })
  @ApiBadRequestResponse({
    description: 'Request validation failed',
  })
  async create(@Body() dto: CreateUserRequestDto): Promise<UserResponseDto> {
    const user = await this.usersService.create(mapCreateUserRequest(dto));
    return toUserResponseDto(user);
  }
}
```

- Add endpoint decorators only after reading the actual request and response path.
- Document expected failure responses when they are part of the real controller behavior.
- Reuse repository auth decorators or schema helpers when they already exist.

## DTO field documentation

```ts
export class CreateUserRequestDto {
  @ApiProperty({
    example: 'user@example.com',
    description: 'User email address',
  })
  @IsEmail()
  email!: string;

  @ApiProperty({
    minLength: 8,
    description: 'Plain-text password before hashing',
  })
  @IsString()
  @MinLength(8)
  password!: string;
}

export class UserResponseDto {
  @ApiProperty({
    example: 'user_1',
  })
  id!: string;

  @ApiProperty({
    example: 'user@example.com',
  })
  email!: string;
}
```

- Keep Swagger metadata aligned with validation decorators and actual runtime shape.
- Use `@ApiPropertyOptional` for fields that are truly optional in the API contract.
- Do not annotate internal-only entities just because they are classes.

## Wrapped and paginated responses

```ts
@ApiOkResponse({
  schema: {
    allOf: [
      { $ref: getSchemaPath(PaginatedResponseDto) },
      {
        properties: {
          items: {
            type: 'array',
            items: { $ref: getSchemaPath(UserResponseDto) },
          },
        },
      },
    ],
  },
})
```

- Prefer existing pagination or envelope helpers when the repository already has them.
- Document the real wrapper shape returned after interceptors or serializers run.
- Avoid forcing a DTO wrapper when the project already uses schema builders for generic responses.
