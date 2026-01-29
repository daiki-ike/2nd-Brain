$csvPath = "c:\Users\daiki\Product\2nd-Brain\2nd-Brain\01_プロジェクト\記録 2280c5b764cf808ea5c6d811caadfc39_all.csv"
$targetDir = "c:\Users\daiki\Product\2nd-Brain\2nd-Brain\05_日誌"
$headerPath = "c:\Users\daiki\Product\2nd-Brain\2nd-Brain\01_プロジェクト\header.txt"

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$data = Import-Csv -Path $csvPath -Encoding UTF8
$headerStr = Get-Content -Path $headerPath -Raw -Encoding UTF8
$headerStr = $headerStr.Trim()

foreach ($row in $data) {
    $url = $row.URL
    $dateStr = ""
    
    foreach ($prop in $row.PSObject.Properties) {
        if ($prop.Value -match "^\d{4}.+\d{1,2}.+\d{1,2}.+$") {
            $dateStr = $prop.Value
            break
        }
    }
    
    if (-not $url -or -not $dateStr) { continue }

    if ($dateStr -match "(\d{4})\D+(\d{1,2})\D+(\d{1,2})") {
        $year = $matches[1]
        $month = $matches[2].PadLeft(2, '0')
        $day = $matches[3].PadLeft(2, '0')
        $fileName = "$year-$month-$day.md"
        $filePath = Join-Path -Path $targetDir -ChildPath $fileName
    } else {
        continue
    }

    $appendContent = "`n`n$headerStr`n- URL: $url`n"

    if (Test-Path $filePath) {
        $currentContent = Get-Content -Path $filePath -Raw -Encoding UTF8
        if ($currentContent -notmatch [regex]::Escape($url)) {
            Add-Content -Path $filePath -Value $appendContent -Encoding UTF8
            Write-Output "Updated: $fileName"
        } else {
            Write-Output "Skipped: $fileName"
        }
    } else {
        $newContent = "# $($year)-$($month)-$($day)`n$appendContent"
        Set-Content -Path $filePath -Value $newContent -Encoding UTF8
        Write-Output "Created: $fileName"
    }
}
