import { describe, it, expect } from 'vitest';
import { first } from './first';

describe("first", () => {
  it("first of non-empty", () => {
    expect(first([5, 6])).toBe(5);
  });
  it("null for empty", () => {
    expect(first([])).toBe(null);
  });
});
