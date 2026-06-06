import { describe, it, expect } from 'vitest';
import { inRange } from './in-range';

describe("inRange", () => {
  it("5 is in 1..10", () => {
    expect(inRange(5, 1, 10)).toBe(true);
  });
  it("11 is out of 1..10", () => {
    expect(inRange(11, 1, 10)).toBe(false);
  });
});
