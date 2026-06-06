import { describe, it, expect } from 'vitest';
import { shout } from './shout';

describe("shout", () => {
  it("shouts hi", () => {
    expect(shout('hi')).toBe('HI!');
  });
  it("shouts go", () => {
    expect(shout('go')).toBe('GO!');
  });
});
