# js-bench — Verdict repair-loop fixtures

Deliberately-buggy JavaScript/TypeScript exercises used to exercise the **Verdict**
autonomous test-repair loop. Each `<name>.test.ts` asserts the intended behavior;
the paired `<name>.ts` contains a planted runtime bug. The loop reads the failing
test, generates a patch to the source, verifies it in a sandbox, and an LLM judge
scores it.

These files are intentionally wrong — they are test fixtures, not reference solutions.
