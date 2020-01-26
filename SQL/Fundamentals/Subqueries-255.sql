## 2. Subqueries ##

SELECT Major, Unemployment_rate FROM recent_grads WHERE Unemployment_rate < (SELECT AVG(Unemployment_rate) FROM recent_grads) ORDER BY Unemployment_rate

## 3. Subquery In SELECT ##

SELECT CAST(COUNT(*) as float) / CAST((SELECT COUNT(*) from recent_grads) as float) proportion_abv_avg FROM recent_grads WHERE ShareWomen > (SELECT  AVG(ShareWomen) from recent_grads)

## 5. Building Complex Subqueries ##

SELECT AVG( CAST(Sample_size as float)/ CAST(Total as float)) avg_ratio FROM recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

SELECT Major, Major_category, CAST( Sample_size as float)/CAST(Total as float) ratio from recent_grads
WHERE ratio > (SELECT AVG(CAST(Sample_size as flot)/CAST(Total as float)) avg_ratio FROM recent_grads)