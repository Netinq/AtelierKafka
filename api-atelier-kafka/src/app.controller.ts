import { Controller, Get, Res } from '@nestjs/common';
import { Response } from 'express';
import { createReadStream } from 'fs';

@Controller()
export class AppController {
  constructor() {}

  @Get()
  getCSV(@Res() res: Response) {
    res.sendFile('./src/ci_vcub_p.csv', { root: '.' });
  }
}
