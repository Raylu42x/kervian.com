const fs = require('fs');
const path = require('path');

module.exports = function () {
  try {
    const raw = fs.readFileSync(path.join(__dirname, '../banner.md'), 'utf8');
    const match = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
    if (!match) return { active: false, message: '' };
    const active = /^\s*active:\s*true\s*$/m.test(match[1]);
    return { active, message: match[2].trim() };
  } catch (e) {
    return { active: false, message: '' };
  }
};
