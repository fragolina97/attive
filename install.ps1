$CommandsDir = "$env:USERPROFILE\.claude\commands"
$SkillsDir = "$env:USERPROFILE\.claude\skills"

New-Item -ItemType Directory -Force -Path $CommandsDir | Out-Null
New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null

Write-Host "Installing Claude Code skills..."
Copy-Item -Path "commands\*" -Destination $CommandsDir -Recurse -Force
Copy-Item -Path "skills\*" -Destination $SkillsDir -Recurse -Force
Write-Host "Done! Skills installed to:"
Write-Host "  $CommandsDir"
Write-Host "  $SkillsDir"
