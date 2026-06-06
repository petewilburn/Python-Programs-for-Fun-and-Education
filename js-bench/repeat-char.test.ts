import { describe, it, expect } from 'vitest';
import { repeatChar } from './repeat-char';

describe("repeatChar", () => {
  it("repeats x three times", () => {
    expect(repeatChar('x', 3)).toBe('xxx');
  });
  it("repeats a once", () => {
    expect(repeatChar('a', 1)).toBe('a');
  });
});
