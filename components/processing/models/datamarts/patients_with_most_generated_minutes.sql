WITH sources AS (

  SELECT
	sum(steps * 0.002) AS minutes,
    external_id AS patient_id
  FROM
    {{ ref('steps_intermediate')}}
  GROUP BY
    patient_id

  UNION ALL

  SELECT
    minutes,
	external_id AS patient_id
  FROM
    {{ ref('exercises_intermediate')}}
),
ranked AS (
  SELECT
    RANK() OVER (ORDER BY SUM(minutes) DESC) AS patient_rank,
	SUM(minutes) AS total_minutes,
    patient_id
  FROM
    sources
  GROUP BY
    patient_id
)
SELECT
  p.patient_id,
  p.first_name,
  p.lASt_name,
  p.country,
  r.total_minutes
FROM
  patients p LEFT JOIN ranked r ON p.patient_id = r.patient_id
WHERE
  patient_rank = 1