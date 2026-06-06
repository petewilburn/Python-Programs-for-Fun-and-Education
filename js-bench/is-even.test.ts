import { describe, it, expect } from 'vitest';
import { isEven } from './is-even';

describe("isEven", () => {
  it("4 is even", () => {
    expect(isEven(4)).toBe(true);
  });
  it("7 is not even", () => {
    expect(isEven(7)).toBe(false);
  });
});
