create table if not exists orders (
  id integer primary key autoincrement,
  customer_name text not null,
  question text not null,
  cards text not null,
  status text not null default 'new',
  created_at text not null default current_timestamp
);

create table if not exists drafts (
  id integer primary key autoincrement,
  order_id integer not null references orders(id),
  body text not null,
  status text not null default 'pending',
  created_at text not null default current_timestamp
);

create table if not exists approvals (
  id integer primary key autoincrement,
  draft_id integer not null references drafts(id),
  status text not null default 'pending',
  reviewer_note text not null default '',
  updated_at text not null default current_timestamp
);

create table if not exists run_logs (
  id integer primary key autoincrement,
  event text not null,
  detail text not null,
  created_at text not null default current_timestamp
);

