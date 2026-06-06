import { describe, it, expect } from 'vitest';
import { safeDivide } from './safe-divide';

describe("safeDivide", () => {
  it("divides 10 by 2", () => {
    expect(safeDivide(10, 2)).toBe(5);
  });
  it("null on divide by zero", () => {
    expect(safeDivide(5, 0)).toBe(null);
  });
});
