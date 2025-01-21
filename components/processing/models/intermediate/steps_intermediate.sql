SELECT
  id,
  external_id,
  steps,
  (submission_time AT TIME ZONE 'UTC')::TIMESTAMP AS submission_time,
  (updated_at AT TIME ZONE 'UTC')::TIMESTAMP AS updated_at
FROM
  {{ source('user_activity', 'steps')}}
{% if is_incremental() %}
  WHERE
    submission_time >= NOW() - INTERVAL '1 day'
{% endif %}
