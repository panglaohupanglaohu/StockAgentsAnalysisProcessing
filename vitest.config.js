import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    environment: 'jsdom',
    include: ['src/frontend/__tests__/**/*.test.js'],
    restoreMocks: true,
  },
});
