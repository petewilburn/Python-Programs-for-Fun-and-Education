import { describe, it, expect } from 'vitest';
import { isEmpty } from './is-empty';

describe("isEmpty", () => {
  it("empty array is empty", () => {
    expect(isEmpty([])).toBe(true);
  });
  it("non-empty is not empty", () => {
    expect(isEmpty([1])).toBe(false);
  });
});
