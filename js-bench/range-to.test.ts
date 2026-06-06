import { describe, it, expect } from 'vitest';
import { rangeTo } from './range-to';

describe("rangeTo", () => {
  it("range to 3 is inclusive", () => {
    expect(rangeTo(3)).toEqual([1, 2, 3]);
  });
  it("range to 1", () => {
    expect(rangeTo(1)).toEqual([1]);
  });
});
