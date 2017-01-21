function urlify(url) {
  let result = "";
  url.split('').forEach( function(c) {
    if (c === ' ') {
      result += '%20';
    } else {
      result += c;
    }
  });

  return result;
}

console.log(urlify("bart mach dude"));
