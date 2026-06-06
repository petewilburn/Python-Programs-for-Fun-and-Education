import { describe, it, expect } from 'vitest';
import { unique } from './unique';

describe("unique", () => {
  it("dedupes repeats", () => {
    expect(unique([1, 1, 2])).toEqual([1, 2]);
  });
  it("collapses all same", () => {
    expect(unique([3, 3, 3])).toEqual([3]);
  });
});
