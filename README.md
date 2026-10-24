# Capital Growth — CI/CD workshop

A small compound-interest Python program designed to demonstrate **GitHub Actions pipelines**.

## Run

```bash
python -m pip install -e '.[dev]'
capital-growth --initial 1000 --target 200000 --rate 0.03
make lint
make test
make security
make build
```

The original example reaches its target after **180 years**.

## CI pipeline (Pull Request and main)

```text
prepare
  ├── lint (Ruff + formatting)
  ├── unit-tests (Python 3.11, 3.12, 3.13 + coverage)
  └── security (Bandit + pip-audit)
           ↓
         package (wheel + sdist + metadata)
           ↓
         smoke-test (install wheel and run CLI)
           ↓
         summary
```

Each **job** is displayed separately in GitHub Actions; each job has several **steps**.
Some steps intentionally only print context so students can see the execution order.

## CD pipeline (tag)

```text
validate-tag → build-release (tests + packaging) → publish (GitHub Release)
```

After merging the PR, create a version:

```bash
git checkout main
git pull
git tag v1.0.0
git push origin v1.0.0
```

Then open the **Actions** and **Releases** tabs.

## Live demonstration

1. Create a feature branch and a PR.
2. Intentionally change `balances[-1] * (1 + rate)` to `balances[-1] * (1 - rate)`.
3. Observe the failing test job; fix the regression and push.
4. Observe parallel jobs and the final package artifact.
5. Merge after all checks are green.
6. Push `v1.0.0`; observe the separate CD workflow.
7. Download the wheel from the release and install it in a clean environment.

## Governance

Recommended: protect `main`, require PRs and passing CI checks, and restrict tag creation to trusted maintainers. GitHub repository rules are not configured automatically by this PR.

## Limits

This is a teaching demo, not financial advice. Floating point arithmetic is sufficient for this example, but real monetary accounting should use Decimal. Publishing to GitHub Releases demonstrates continuous delivery, not automatic production deployment.
