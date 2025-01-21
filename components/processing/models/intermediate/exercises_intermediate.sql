SELECT
  id,
  external_id,
  minutes,
  (completed_at AT TIME ZONE 'UTC')::TIMESTAMP AS completed_at,
  (updated_at AT TIME ZONE 'UTC')::TIMESTAMP AS updated_at
FROM
  {{ source('user_activity', 'exercises')}}
{% if is_incremental() %}
WHERE
  completed_at >= NOW() - INTERVAL '1 day'
{% endif %}
