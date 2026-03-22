param(
    [string]$Message = ""
)

Set-Location $PSScriptRoot

# --- Build: regenerate HTML from source markdown ---
$pages = @(
    @{ src = "skadestabilitet_teori.md";                out = "docs\skadestabilitet_teori.html" },
    @{ src = "skadestabilitet_oppgaver.md";             out = "docs\skadestabilitet_oppgaver.html" },
    @{ src = "skadestabilitet_obligatorisk_oppgave.md"; out = "docs\skadestabilitet_obligatorisk_oppgave.html" }
)
foreach ($p in $pages) {
    pandoc -s --mathjax -o $p.out $p.src
    if ($LASTEXITCODE -ne 0) { Write-Error "pandoc feilet for $($p.src)"; exit 1 }
    Write-Host "Bygget: $($p.out)"
}

# --- Post-processing ---
$hint = ' <em style="font-size:0.85em; color:#666;">(Høyreklikk → Lagre lenke som... om filen åpnes i nettleseren i stedet for å lastes ned)</em>'
foreach ($p in $pages) {
    $c = Get-Content $p.out -Raw -Encoding UTF8
    $c = [regex]::Replace($c, '<figcaption aria-hidden="true">.*?</figcaption>', '', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    $c = [regex]::Replace($c, '(href="exports/[^"]+\.(ipynb|csv)">[^<]+</a>)(</p>)', "`$1$hint`$3", [System.Text.RegularExpressions.RegexOptions]::Singleline)
    Set-Content $p.out $c -Encoding UTF8 -NoNewline
}

# Show current changes
git status --short
if ($LASTEXITCODE -ne 0) { exit 1 }

$changed = git diff --name-only HEAD
if (-not $changed) {
    Write-Host "Ingen endringer å publisere."
    exit 0
}

# Require a commit message
if (-not $Message) {
    $Message = Read-Host "Commit-melding"
}
if (-not $Message) {
    Write-Error "Commit-melding kan ikke vaere tom."
    exit 1
}

git add docs/
git commit -m $Message
if ($LASTEXITCODE -ne 0) { exit 1 }

git push
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "Publisert: $Message"
