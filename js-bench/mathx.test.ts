import { describe, it, expect } from 'vitest';
import { square } from './mathx';

describe("square", () => {
  it("squares 3", () => {
    expect(square(3)).toBe(9);
  });
  it("squares 5", () => {
    expect(square(5)).toBe(25);
  });
});
