 <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>
<head>
  <title>PHP/YAZ</title>
</head>
<body>
<?
    $host = $_GET['host'];
    $term = $_GET['term'];
    $num_hosts = count($host);
    if (empty($term) || count($host) == 0)
    {
        echo '<form method="get">
                <input type="checkbox" name="host[]" value="bagel.indexdata.dk/gils">
            GILS test
                <input type="checkbox" name="host[]" value="www.bibhit.dk">
                Bibhit
                <input type="checkbox" checked="1" name="host[]" value="blpcz.bl.uk:21021/BLPC-ALL">
                British Library
<br>
RPN Query:
<input type="text" size="30" name="term">
<input type="submit" name="action" value="Search">
        ';        
    }
    else
    {
        echo 'You searced for ' . htmlspecialchars($term) . '<br>';
        for ($i = 0; $i < $num_hosts; $i++) {
            $id[] = yaz_connect($host[$i]);
            yaz_syntax($id[$i],"sutrs");
            yaz_search($id[$i],"rpn",$term);
        }
        yaz_wait();
        for ($i = 0;  $i <$num_hosts; $i++)
        {
            echo '<hr>' . $host[$i] . ":";
            $error = yaz_error($id[$i]);
            if (!empty($error)) {
                echo "Error: $error";
            } else {
                $hits = yaz_hits($id[$i]);
                echo "Result Count $hits";
            }
            echo '<dl>';
            for ($p = 1; $p <= 10; $p++)
            {
                $rec = yaz_record($id[$i],$p,"string");
                if (empty($rec)) continue;
                echo "<dt><b>$p</b></dt><dd>";
                echo ereg_replace("\n", "<br>\n",$rec);
                echo "</dd>";
            }
            echo '</dl>';
        }
    }
?>
<br>
<a href="mult.phps">View Source</a>
</body>
</html>
