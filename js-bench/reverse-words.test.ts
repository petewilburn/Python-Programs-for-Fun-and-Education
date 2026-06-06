import { describe, it, expect } from 'vitest';
import { reverseWords } from './reverse-words';

describe("reverseWords", () => {
  it("reverses word order", () => {
    expect(reverseWords('a b c')).toBe('c b a');
  });
  it("reverses two words", () => {
    expect(reverseWords('one two')).toBe('two one');
  });
});
