import { describe, it, expect } from 'vitest';
import { fullName } from './full-name';

describe("fullName", () => {
  it("orders first then last", () => {
    expect(fullName('Ada', 'Lovelace')).toBe('Ada Lovelace');
  });
  it("orders Grace Hopper", () => {
    expect(fullName('Grace', 'Hopper')).toBe('Grace Hopper');
  });
});
