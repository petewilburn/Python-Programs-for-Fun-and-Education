import { describe, it, expect } from 'vitest';
import { applyDiscount } from './discount';

describe("applyDiscount", () => {
  it("20% off 100", () => {
    expect(applyDiscount(100, 0.2)).toBe(80);
  });
  it("10% off 50", () => {
    expect(applyDiscount(50, 0.1)).toBe(45);
  });
});
