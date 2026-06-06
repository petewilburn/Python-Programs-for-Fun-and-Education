import { describe, it, expect } from 'vitest';
import { minutesToSeconds } from './minutes-to-seconds';

describe("minutesToSeconds", () => {
  it("2 minutes", () => {
    expect(minutesToSeconds(2)).toBe(120);
  });
  it("1 minute", () => {
    expect(minutesToSeconds(1)).toBe(60);
  });
});
