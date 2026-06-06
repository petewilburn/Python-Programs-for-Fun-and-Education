import { describe, it, expect } from 'vitest';
import { average } from './average';

describe("average", () => {
  it("avg 4 and 6", () => {
    expect(average(4, 6)).toBe(5);
  });
  it("avg 10 and 20", () => {
    expect(average(10, 20)).toBe(15);
  });
});
