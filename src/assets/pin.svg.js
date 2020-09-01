export default (char) => `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="24px" height="24px">
  <path d="M0 0h24v24H0z" fill="none" />
  <path d="M 12,2 C 8.13,2 5,5.13 5,9 c 0,5.25 7,13 7,13 0,0 7,-7.75 7,-13 0,-3.87 -3.13,-7 -7,-7 z"/>
  <text fill="white" font-weight="bold" font-family="sans-serif" font-size="14" x="50%" y="45%" dominant-baseline="middle" text-anchor="middle">${char}</text>
</svg>
`;
