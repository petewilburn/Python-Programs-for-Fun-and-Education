import { describe, it, expect } from 'vitest';
import { sum } from './sum';

describe("sum", () => {
  it("sums three numbers", () => {
    expect(sum([1, 2, 3])).toBe(6);
  });
  it("empty sums to zero", () => {
    expect(sum([])).toBe(0);
  });
});
