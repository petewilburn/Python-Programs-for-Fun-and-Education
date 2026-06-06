import { describe, it, expect } from 'vitest';
import { greet } from './greet';

describe("greet", () => {
  it("greets Sam", () => {
    expect(greet('Sam')).toBe('Hello, Sam');
  });
  it("greets Ada", () => {
    expect(greet('Ada')).toBe('Hello, Ada');
  });
});
