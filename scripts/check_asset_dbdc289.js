// DBDC-289: verify each relative image reference in the changed Markdown resolves from its own directory
const fs = require("fs");
const path = require("path");
const root = "/home/node/.local/share/docbits-docs-nightly/wt-dbdc289";
const files = [
  "readme/end-user-and-partner-section/end-user-section/supplier-statistics.md",
  "readme/administration-and-setup/settings/document-processing/module/README.md",
];
let ok = true;
for (const rel of files) {
  const abs = path.join(root, rel);
  const text = fs.readFileSync(abs, "utf8");
  const refs = [...text.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)].map(m => m[1])
    .concat([...text.matchAll(/<img src="([^"]+)"/g)].map(m => m[1]));
  for (const ref of refs) {
    if (/^https?:/.test(ref)) continue;
    const target = path.resolve(path.dirname(abs), ref.split("#")[0]);
    const exists = fs.existsSync(target);
    console.log((exists ? "OK  " : "MISS") + " " + rel + " -> " + ref);
    if (!exists) ok = false;
  }
  // also check relative doc links
  const links = [...text.matchAll(/\]\((?!https?:)([^)#]+)(?:#[^)]*)?\)/g)].map(m => m[1]);
  for (const ref of links) {
    const target = path.resolve(path.dirname(abs), ref);
    const exists = fs.existsSync(target);
    console.log((exists ? "OK  " : "MISS") + " " + rel + " [link] " + ref);
    if (!exists) ok = false;
  }
}
console.log(ok ? "ASSET_OK" : "ASSET_FAIL");
process.exit(ok ? 0 : 1);
