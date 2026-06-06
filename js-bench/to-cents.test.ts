import { describe, it, expect } from 'vitest';
import { toCents } from './to-cents';

describe("toCents", () => {
  it("2 dollars is 200 cents", () => {
    expect(toCents(2)).toBe(200);
  });
  it("half dollar is 50 cents", () => {
    expect(toCents(0.5)).toBe(50);
  });
});
