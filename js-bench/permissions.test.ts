import { describe, it, expect } from 'vitest';
import { canEdit } from './permissions';

describe("canEdit", () => {
  it("editor can edit", () => {
    expect(canEdit({ role: 'editor' })).toBe(true);
  });
  it("viewer cannot edit", () => {
    expect(canEdit({ role: 'viewer' })).toBe(false);
  });
});
