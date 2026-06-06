import { describe, it, expect } from 'vitest';
import { add } from './add';

describe("add", () => {
  it("adds 2 + 3", () => {
    expect(add(2, 3)).toBe(5);
  });
  it("adds 10 + 5", () => {
    expect(add(10, 5)).toBe(15);
  });
});
