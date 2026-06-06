import { describe, it, expect } from 'vitest';
import { rectArea } from './rect-area';

describe("rectArea", () => {
  it("area 3 x 4", () => {
    expect(rectArea(3, 4)).toBe(12);
  });
  it("area 5 x 2", () => {
    expect(rectArea(5, 2)).toBe(10);
  });
});
