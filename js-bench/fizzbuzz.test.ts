import { describe, it, expect } from 'vitest';
import { fizzbuzz } from './fizzbuzz';

describe("fizzbuzz", () => {
  it("15 is FizzBuzz", () => {
    expect(fizzbuzz(15)).toBe('FizzBuzz');
  });
  it("3 is Fizz", () => {
    expect(fizzbuzz(3)).toBe('Fizz');
  });
  it("5 is Buzz", () => {
    expect(fizzbuzz(5)).toBe('Buzz');
  });
});
