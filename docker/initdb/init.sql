-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Create meals table with embedding support
CREATE TABLE meals (
  id SERIAL PRIMARY KEY,
  description TEXT,
  calories INT,
  protein FLOAT,
  carbs FLOAT,
  embedding VECTOR(1536)
);

-- Optional: Create index for fast similarity search
CREATE INDEX ON meals USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

