import { describe, it, expect } from 'vitest';
import { countVowels } from './count-vowels';

describe("countVowels", () => {
  it("counts all five vowels", () => {
    expect(countVowels('aeiou')).toBe(5);
  });
  it("no vowels", () => {
    expect(countVowels('xyz')).toBe(0);
  });
});
