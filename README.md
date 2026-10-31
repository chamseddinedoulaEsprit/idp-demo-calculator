# idp-demo-calculator

Public demo repository for the Intelligent Delivery Platform: a tiny calculator,
unit tests and a 3-job GitHub Actions workflow (lint -> test -> package).

Each failure scenario is one commit that breaks the CI, followed by the commit that fixes it:

| Scenario | Failing job | Error in the log |
|---|---|---|
| broken / fixed | test | `AssertionError` (add subtracts) |
| deps-broken / deps-fixed | test (install) | `No matching distribution found for requests==99.0.0` |
| syntax-broken / syntax-fixed | lint | `SyntaxError: expected ':'` |
| module-missing / module-fixed | test | `ModuleNotFoundError: No module named 'numpy'` |
| exception-broken / exception-fixed | test | `ZeroDivisionError` in `divide` |
| package-broken / package-fixed | package | `tar: LICENSE: Cannot stat: No such file or directory` |
