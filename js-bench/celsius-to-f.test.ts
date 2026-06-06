import { describe, it, expect } from 'vitest';
import { celsiusToF } from './celsius-to-f';

describe("celsiusToF", () => {
  it("freezing point", () => {
    expect(celsiusToF(0)).toBe(32);
  });
  it("boiling point", () => {
    expect(celsiusToF(100)).toBe(212);
  });
});
