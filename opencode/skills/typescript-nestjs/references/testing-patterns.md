# Testing Patterns

Use this file when the main skill is not enough for testing-module setup, mock providers, or e2e structure.

## Contents

- Unit test with a mocked provider
- Integration test for module wiring
- Guard or interceptor test
- E2E skeleton
- Module override for external dependencies

## Unit test with a mocked provider

```ts
describe('UsersService', () => {
  let service: UsersService;
  const userRepository = {
    create: jest.fn(),
  };

  beforeEach(async () => {
    const moduleRef = await Test.createTestingModule({
      providers: [
        UsersService,
        {
          provide: USER_REPOSITORY,
          useValue: userRepository,
        },
      ],
    }).compile();

    service = moduleRef.get(UsersService);
    jest.clearAllMocks();
  });

  it('returns the created user after persistence', async () => {
    userRepository.create.mockResolvedValue({
      id: 'user_1',
      email: 'a@example.com',
    });

    await expect(
      service.create({ email: 'a@example.com', password: 'password-1' }),
    ).resolves.toEqual({
      id: 'user_1',
      email: 'a@example.com',
    });
  });
});
```

- Mock only the provider boundary owned by the service under test.
- Assert domain behavior and returned shape, not Nest internals.
- Reset mocks between tests to keep failure signals local.

## Integration test for module wiring

```ts
describe('UsersModule', () => {
  it('wires the service and repository contract', async () => {
    const moduleRef = await Test.createTestingModule({
      imports: [UsersModule],
    })
      .overrideProvider(USER_REPOSITORY)
      .useValue({
        create: jest.fn(),
        findById: jest.fn(),
      })
      .compile();

    expect(moduleRef.get(UsersService)).toBeInstanceOf(UsersService);
  });
});
```

- Use integration tests to verify module imports, providers, and overrides without starting the whole app.
- Keep the assertion focused on wiring or a narrow collaboration path.

## Guard or interceptor test

```ts
describe('AuthGuard', () => {
  it('allows requests with a valid user on the request context', async () => {
    const guard = new AuthGuard();
    const context = {
      switchToHttp: () => ({
        getRequest: () => ({ user: { id: 'user_1' } }),
      }),
    } as ExecutionContext;

    expect(guard.canActivate(context)).toBe(true);
  });

  it('rejects requests without an authenticated user', async () => {
    const guard = new AuthGuard();
    const context = {
      switchToHttp: () => ({
        getRequest: () => ({ user: null }),
      }),
    } as ExecutionContext;

    expect(guard.canActivate(context)).toBe(false);
  });
});
```

- Keep framework-heavy tests small and focused on branch behavior.
- Prefer helper builders for repetitive `ExecutionContext` setup.

## E2E skeleton

```ts
describe('UsersController (e2e)', () => {
  let app: INestApplication;

  beforeAll(async () => {
    const moduleRef = await Test.createTestingModule({
      imports: [AppModule],
    }).compile();

    app = moduleRef.createNestApplication();
    app.useGlobalPipes(new ValidationPipe({ whitelist: true, transform: true }));
    await app.init();
  });

  afterAll(async () => {
    await app.close();
  });

  it('creates a user', async () => {
    await request(app.getHttpServer())
      .post('/users')
      .send({ email: 'a@example.com', password: 'password-1' })
      .expect(201)
      .expect(({ body }) => {
        expect(body.email).toBe('a@example.com');
      });
  });

  it('rejects an invalid payload', async () => {
    await request(app.getHttpServer())
      .post('/users')
      .send({ email: 'invalid-email', password: 'short' })
      .expect(400);
  });
});
```

- Use e2e tests to verify wiring, validation, auth, and response contracts together.
- Apply the same global pipes or filters the real app relies on when the behavior matters.
- Cover one representative failure path for each critical entry point.

## Module override for external dependencies

```ts
beforeAll(async () => {
  const moduleRef = await Test.createTestingModule({
    imports: [AppModule],
  })
    .overrideProvider(USER_REPOSITORY)
    .useValue({
      create: jest.fn(),
      findById: jest.fn(),
    })
    .compile();

  app = moduleRef.createNestApplication();
  await app.init();
});
```

- Override providers at the Nest testing module boundary when the real dependency is slow, flaky, or external.
- Keep the override shape aligned with the contract consumed by the application service.
- Prefer explicit provider overrides over hidden global mocks for e2e-style tests.
