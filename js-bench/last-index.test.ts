import { describe, it, expect } from 'vitest';
import { lastIndex } from './last-index';

describe("lastIndex", () => {
  it("index of last of three", () => {
    expect(lastIndex([1, 2, 3])).toBe(2);
  });
  it("index of last of one", () => {
    expect(lastIndex(['a'])).toBe(0);
  });
});
