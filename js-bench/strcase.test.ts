import { describe, it, expect } from 'vitest';
import { capitalize } from './strcase';

describe("capitalize", () => {
  it("capitalizes hello", () => {
    expect(capitalize('hello')).toBe('Hello');
  });
  it("capitalizes world", () => {
    expect(capitalize('world')).toBe('World');
  });
});
