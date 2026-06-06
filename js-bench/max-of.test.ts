import { describe, it, expect } from 'vitest';
import { maxOf } from './max-of';

describe("maxOf", () => {
  it("max of three", () => {
    expect(maxOf([3, 1, 2])).toBe(3);
  });
  it("null for empty", () => {
    expect(maxOf([])).toBe(null);
  });
});
