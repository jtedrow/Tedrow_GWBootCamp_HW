Sub multiple_run()
    Dim xSh As Worksheet
    Application.ScreenUpdating = False
    For Each xSh In Worksheets
        xSh.Select
        Call ticker_summary
    Next
    Application.ScreenUpdating = True
End Sub

Sub ticker_summary()

'Set variables
Dim ticker As String
Dim volume_total As Double
    volume_total = 0
Dim volume As Long
Dim summary_table_row As Integer
    summary_table_row = 2
Dim lastrow As Long
    lastrow = Cells(Rows.Count, 1).End(xlUp).Row
Dim open_price As Double
Dim close_price As Double
Dim yearly_change As Double
Dim percent_change As Double

'Give column names
Range("J1").Value = "Ticker"
Range("K1").Value = "Yearly Volume"
Range("L1").Value = "Yearly Change"
Range("M1").Value = "Percent Change"
Range("P1").Value = "Ticker"
Range("Q1").Value = "Value"
Range("O2").Value = "Greatest % Increase"
Range("O3").Value = "Greatest % Decrease"
Range("O4").Value = "Greatest Total Volume"
Range("J1:M1").Interior.ColorIndex = "15"
Range("J1:M1").Font.Bold = True
Range("O2:O4").Interior.ColorIndex = "15"
Range("O2:O4").Font.Bold = True
Range("P1:Q1").Interior.ColorIndex = "15"
Range("P1:Q1").Font.Bold = True
    
       
For i = 2 To lastrow

    If i = 2 Then
        open_price = Cells(i, 3)
        volume = Cells(i, 7)
        close_price = Cells(i, 6)
        volume_total = volume_total + volume
    
    Else
        
        'Store daily volume and daily close
        volume = Cells(i, 7)
        close_price = Cells(i, 6)
            
        If (Cells(i, 1).Value <> Cells(i + 1, 1).Value) Then
        
            'Store ticker name
            ticker = Cells(i, 1).Value
        
            'Add last day of volume
            volume_total = volume_total + volume
            
            'Calculate yearly change and percent change
            yearly_change = close_price - open_price
            
            If open_price <> 0 Then
                percent_change = yearly_change / open_price
            
            Else
                percent_change = 0
            End If
            
        
            'Print ticker and cumulative volume in columns J and K
            Range("J" & summary_table_row).Value = ticker
            Range("K" & summary_table_row).Value = Format(volume_total, "0,000")
            Range("L" & summary_table_row).Value = yearly_change
            Range("M" & summary_table_row).Value = FormatPercent(percent_change)
            
                If yearly_change >= 0 Then
                    Range("L" & summary_table_row).Interior.ColorIndex = "10"
                Else
                    Range("L" & summary_table_row).Interior.ColorIndex = "3"
                
                End If
                
            'Store open price
            open_price = Cells(i + 1, 3)
                               
            'Move to the next row in the summary table
            summary_table_row = summary_table_row + 1
        
            'Reset volume total to 0 as we are moving to the next ticker
            volume_total = 0
            
        Else
            'Add today's volume to the total volume
            volume_total = volume_total + volume
            
        End If
        
    End If
    
Next i

Dim lastrow_summary As Integer
    lastrow_summary = Cells(Rows.Count, 10).End(xlUp).Row

'Largest volume
max_volume = WorksheetFunction.Max(Range("K2:K" & lastrow_summary))
max_volume_ticker = WorksheetFunction.Match(max_volume, Range("K2:K" & lastrow_summary), 0)
Cells(4, 16).Value = Range("J" & max_volume_ticker + 1)
Cells(4, 17).Value = Format(max_volume, "0,000")

'Greatest % Increase
max_increase = WorksheetFunction.Max(Range("M2:M" & lastrow_summary))
max_increase_ticker = WorksheetFunction.Match(max_increase, Range("M2:M" & lastrow_summary), 0)
Cells(2, 16).Value = Range("J" & max_increase_ticker + 1)
Cells(2, 17).Value = FormatPercent(max_increase)

'Greatest % Decrease
max_decrease = WorksheetFunction.Min(Range("M2:M" & lastrow_summary))
max_decrease_ticker = WorksheetFunction.Match(max_decrease, Range("M2:M" & lastrow_summary), 0)
Cells(3, 16).Value = Range("J" & max_decrease_ticker + 1)
Cells(3, 17).Value = FormatPercent(max_decrease)

Range("J1:Q1000").Columns.AutoFit
Range("J1:M" & lastrow_summary).Borders.LineStyle = xlContinuous
Range("J1:M" & lastrow_summary).BorderAround _
 ColorIndex:=1, Weight:=xlThick
Range("O1:Q4").Borders.LineStyle = xlContinuous
Range("O1:Q4").BorderAround _
 ColorIndex:=1, Weight:=xlThick

End Sub


