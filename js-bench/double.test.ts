import { describe, it, expect } from 'vitest';
import { double } from './double';

describe("double", () => {
  it("doubles 4", () => {
    expect(double(4)).toBe(8);
  });
  it("doubles 5", () => {
    expect(double(5)).toBe(10);
  });
});
