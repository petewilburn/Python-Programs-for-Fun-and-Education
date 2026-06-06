import { describe, it, expect } from 'vitest';
import { sign } from './sign';

describe("sign", () => {
  it("sign of zero is zero", () => {
    expect(sign(0)).toBe(0);
  });
  it("sign of positive", () => {
    expect(sign(5)).toBe(1);
  });
  it("sign of negative", () => {
    expect(sign(-3)).toBe(-1);
  });
});
