export const repeatChar = (c: string, n: number) => {
  let s = '';
  for (let i = 1; i < n; i++) s += c;
  return s;
};
