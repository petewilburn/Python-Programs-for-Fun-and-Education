import { describe, it, expect } from 'vitest';
import { grade } from './grade';

describe("grade", () => {
  it("90 is an A", () => {
    expect(grade(90)).toBe('A');
  });
  it("95 is an A", () => {
    expect(grade(95)).toBe('A');
  });
  it("80 is a B", () => {
    expect(grade(80)).toBe('B');
  });
});
